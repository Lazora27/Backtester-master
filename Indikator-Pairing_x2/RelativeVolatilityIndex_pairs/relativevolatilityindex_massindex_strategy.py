import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVolatilityIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVolatilityIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'RelativeVolatilityIndex': 1.0,
            'MassIndex': 1.0
        })
    )
