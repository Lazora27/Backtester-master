import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
