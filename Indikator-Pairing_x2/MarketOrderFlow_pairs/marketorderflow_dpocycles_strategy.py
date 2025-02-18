import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'DPOCycles': 1.0
        })
    )
