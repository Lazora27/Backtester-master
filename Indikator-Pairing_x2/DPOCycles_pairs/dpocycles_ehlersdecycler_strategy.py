import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'EhlersDecycler': 1.0
        })
    )
