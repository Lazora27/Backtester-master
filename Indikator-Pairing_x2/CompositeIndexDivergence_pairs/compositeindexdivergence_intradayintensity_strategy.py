import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'IntradayIntensity': 1.0
        })
    )
