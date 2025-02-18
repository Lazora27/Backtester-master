import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LaggingVolatilityIndex_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LaggingVolatilityIndex und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'LaggingVolatilityIndex': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
