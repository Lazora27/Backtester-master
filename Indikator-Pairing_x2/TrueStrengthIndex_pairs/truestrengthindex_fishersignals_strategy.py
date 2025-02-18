import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
