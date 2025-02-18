import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'DonchianVolatility': 1.0
        })
    )
