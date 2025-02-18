import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'FisherSignals': 1.0
        })
    )
