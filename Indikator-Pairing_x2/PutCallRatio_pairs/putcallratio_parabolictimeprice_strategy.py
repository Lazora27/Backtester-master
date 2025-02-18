import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
