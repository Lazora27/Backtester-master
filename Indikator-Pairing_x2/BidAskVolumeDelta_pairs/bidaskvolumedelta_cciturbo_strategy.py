import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'CCITurbo': 1.0
        })
    )
