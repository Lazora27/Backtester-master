import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
