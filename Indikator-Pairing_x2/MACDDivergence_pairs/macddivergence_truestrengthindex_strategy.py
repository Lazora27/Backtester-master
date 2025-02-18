import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
