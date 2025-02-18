import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
