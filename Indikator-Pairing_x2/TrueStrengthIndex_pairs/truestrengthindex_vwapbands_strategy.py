import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
