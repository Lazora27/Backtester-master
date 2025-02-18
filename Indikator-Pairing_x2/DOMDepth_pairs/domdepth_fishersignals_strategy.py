import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'FisherSignals': 1.0
        })
    )
