import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
