import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
