import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
