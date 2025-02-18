import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
