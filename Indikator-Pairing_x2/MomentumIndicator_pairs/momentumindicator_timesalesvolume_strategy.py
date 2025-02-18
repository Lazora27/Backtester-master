import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
