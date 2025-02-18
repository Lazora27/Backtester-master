import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'FisherSignals': 1.0
        })
    )
