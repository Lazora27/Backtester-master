import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeMomentumOscillator_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeMomentumOscillator und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ChandeMomentumOscillator': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
