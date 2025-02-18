import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ShortTermVolatilityIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ShortTermVolatilityIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ShortTermVolatilityIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
