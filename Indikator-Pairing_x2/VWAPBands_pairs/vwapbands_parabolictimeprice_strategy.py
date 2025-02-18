import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
