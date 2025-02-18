import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
