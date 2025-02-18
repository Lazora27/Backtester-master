import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und FisherSignals
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'FisherSignals': 1.0
        })
    )
