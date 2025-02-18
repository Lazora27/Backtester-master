import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
