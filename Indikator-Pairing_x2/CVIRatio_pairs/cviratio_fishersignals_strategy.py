import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FisherSignals': 1.0
        })
    )
