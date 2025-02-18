import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
