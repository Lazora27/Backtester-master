import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'TimeCycle': 1.0
        })
    )
