import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
