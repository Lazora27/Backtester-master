import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
