import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'FisherSignals': 1.0
        })
    )
