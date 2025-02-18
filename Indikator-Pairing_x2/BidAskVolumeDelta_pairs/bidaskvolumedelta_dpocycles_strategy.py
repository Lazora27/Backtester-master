import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'DPOCycles': 1.0
        })
    )
