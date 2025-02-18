import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'DPOCycles': 1.0
        })
    )
