import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'MassIndex': 1.0
        })
    )
