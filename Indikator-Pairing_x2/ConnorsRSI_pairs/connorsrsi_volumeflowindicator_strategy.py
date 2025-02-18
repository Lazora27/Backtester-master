import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
