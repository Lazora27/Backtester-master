import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
