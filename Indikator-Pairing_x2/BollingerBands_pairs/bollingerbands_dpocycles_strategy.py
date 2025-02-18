import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'DPOCycles': 1.0
        })
    )
