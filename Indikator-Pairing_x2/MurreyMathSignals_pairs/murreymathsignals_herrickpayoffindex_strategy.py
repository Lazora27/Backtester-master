import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
