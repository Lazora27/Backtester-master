import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
