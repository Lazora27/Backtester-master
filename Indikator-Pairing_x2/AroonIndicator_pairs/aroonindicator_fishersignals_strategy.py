import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
