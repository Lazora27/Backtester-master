import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
