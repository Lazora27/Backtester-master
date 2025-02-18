import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
