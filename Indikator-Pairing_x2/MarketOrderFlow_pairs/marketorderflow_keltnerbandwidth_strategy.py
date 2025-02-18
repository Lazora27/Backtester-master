import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
