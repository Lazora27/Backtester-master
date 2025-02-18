import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
