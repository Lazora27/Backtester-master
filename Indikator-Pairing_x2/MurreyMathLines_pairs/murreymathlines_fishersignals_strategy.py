import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'FisherSignals': 1.0
        })
    )
