import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
