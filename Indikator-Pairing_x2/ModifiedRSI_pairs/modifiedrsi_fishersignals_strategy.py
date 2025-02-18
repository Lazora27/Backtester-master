import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'FisherSignals': 1.0
        })
    )
