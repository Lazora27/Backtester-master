import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und FisherSignals
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'FisherSignals': 1.0
        })
    )
