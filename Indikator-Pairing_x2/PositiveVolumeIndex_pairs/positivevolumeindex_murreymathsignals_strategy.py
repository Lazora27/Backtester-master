import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
