import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und GannAngles
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'GannAngles': 1.0
        })
    )
