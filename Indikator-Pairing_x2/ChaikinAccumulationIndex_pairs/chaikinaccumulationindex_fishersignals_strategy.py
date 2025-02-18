import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinAccumulationIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinAccumulationIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChaikinAccumulationIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
