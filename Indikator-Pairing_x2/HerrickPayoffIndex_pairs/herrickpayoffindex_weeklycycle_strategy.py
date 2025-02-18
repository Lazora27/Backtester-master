import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
